# Play-Annotation-Generator Annotation Review — QuickScreens_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_41`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 128
- **Validation Warnings:** 148
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 111
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_ScreenBlock` | WR2 | offense | `4` | `4` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR1 | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR1 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 16 | START | 16 | 26 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 26 | END | 16 | 26 |
| ✅ EXACT | `Action_ScreenBlock` | WR2 | `4` | `4` | 27 | START | 27 | 122 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR1 | `2` | `2` | 32 | START | 32 | 52 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `19` | `19` | 41 | START | 41 | 49 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `2` | `2` | 58 | START | 58 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR1 | `2` | `2` | 73 | START | 73 | 130 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 26 | 11 | inferred_complete_timeline |
| `Action_None` | 27 | 40 | 14 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 41 | 49 | 9 | inferred_complete_timeline |
| `Action_None` | 50 | 193 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 89 | 74 | inferred_complete_timeline |
| `Action_None` | 91 | 193 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 32 | 52 | 21 | inferred_complete_timeline |
| `Action_None` | 53 | 57 | 5 | inferred_complete_timeline |
| `Action_SecureCatch` | 58 | 68 | 11 | inferred_complete_timeline |
| `Action_None` | 69 | 72 | 4 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 73 | 130 | 58 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 132 | 145 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_ScreenBlock` | 27 | 122 | 96 | inferred_complete_timeline |
| `Action_None` | 124 | 131 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 115 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 58 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 91 | 76 | inferred_complete_timeline |
| `Action_None` | 97 | 137 | 41 | inferred_complete_timeline |
| `Action_None` | 139 | 171 | 33 | inferred_complete_timeline |
| `Action_None` | 173 | 193 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 26 | 11 | inferred_complete_timeline |
| `Action_None` | 27 | 76 | 50 | inferred_complete_timeline |
| `Action_None` | 81 | 96 | 16 | inferred_complete_timeline |
| `Action_None` | 98 | 145 | 48 | inferred_complete_timeline |
| `Action_None` | 150 | 153 | 4 | inferred_complete_timeline |
| `Action_None` | 162 | 193 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 25 | 10 | inferred_complete_timeline |
| `Action_None` | 34 | 58 | 25 | inferred_complete_timeline |
| `Action_None` | 137 | 183 | 47 | inferred_complete_timeline |
| `Action_None` | 185 | 193 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 89 | 44 | inferred_complete_timeline |
| `Action_None` | 91 | 193 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 30 | 15 | inferred_complete_timeline |
| `Action_None` | 45 | 72 | 28 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_None` | 82 | 93 | 12 | inferred_complete_timeline |
| `Action_None` | 96 | 118 | 23 | inferred_complete_timeline |
| `Action_None` | 124 | 139 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 52 | 37 | inferred_complete_timeline |
| `Action_None` | 58 | 83 | 26 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 193 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 193 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 35 | 20 | inferred_complete_timeline |
| `Action_None` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 60 | 17 | inferred_complete_timeline |
| `Action_None` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_None` | 69 | 113 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 47 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 150 | 135 | inferred_complete_timeline |
| `Action_None` | 155 | 158 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_None` | 44 | 76 | 33 | inferred_complete_timeline |
| `Action_None` | 82 | 119 | 38 | inferred_complete_timeline |
| `Action_None` | 124 | 167 | 44 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 53 | 38 | inferred_complete_timeline |
| `Action_None` | 55 | 59 | 5 | inferred_complete_timeline |
| `Action_None` | 61 | 65 | 5 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_None` | 87 | 93 | 7 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 112 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 193 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 139 | 124 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 179 | 24 | inferred_complete_timeline |
| `Action_None` | 183 | 187 | 5 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 193 | 178 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–25 | 26 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 60–193 | 122 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 61–178 | 113 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 120–193 | 74 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 125–193 | 51 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 174–193 | 20 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 188–193 | 6 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `42` | `47` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `43` | `48` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `44` | `49` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 98 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 46: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [16-115] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-91] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-137] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-171] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-193] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [73-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [132-145] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ScreenBlock' range [27-122] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-131] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-53] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-65] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-93] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-112] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-58] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-25] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-83] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-193] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-35] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-60] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-113] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-193] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-193] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-76] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-119] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-167] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-30] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-72] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-139] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-89] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-193] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-183] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-193] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-151] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-152] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-176] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-193] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>