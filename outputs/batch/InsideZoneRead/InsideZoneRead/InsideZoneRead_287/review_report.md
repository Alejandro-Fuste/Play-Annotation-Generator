# Play-Annotation-Generator Annotation Review — InsideZoneRead_287

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_287`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `0` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `1` | `0` |
| ✅ EXACT | `Action_Keep` | QB | offense | `1` | `0` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `17` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 23 | START | 23 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 26 | START | 26 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `12` | 26 | START | 26 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `17` | 26 | START | 26 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 26 | START | 39 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 26 | START | 26 | 32 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `0` | 34 | END | 23 | 34 |
| ✅ EXACT | `Action_ReadDefender` | QB | `1` | `0` | 41 | START | 41 | 51 |
| ✅ EXACT | `Action_Keep` | QB | `1` | `0` | 52 | START | 52 | 72 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | `1` | `0` | 75 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 101 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 34 | 12 | inferred_complete_timeline |
| `Action_None` | 35 | 40 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 41 | 51 | 11 | inferred_complete_timeline |
| `Action_Keep` | 52 | 72 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 58 | 36 | inferred_complete_timeline |
| `Action_None` | 72 | 210 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 202 | 180 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 210 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 210 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 107 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 32 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 45 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 97 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 101 | 1 | inferred_complete_timeline |
| `Action_None` | 102 | 210 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 32 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 101 | 14 | inferred_complete_timeline |
| `Action_None` | 102 | 146 | 45 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 23 | 31 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 67 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 72 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 32 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 45 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 58 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 83 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 101 | 15 | inferred_complete_timeline |
| `Action_None` | 102 | 121 | 20 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 163 | 195 | 33 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 47 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 93 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 101 | 1 | inferred_complete_timeline |
| `Action_None` | 102 | 210 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 30 | 8 | inferred_complete_timeline |
| `Action_None` | 37 | 44 | 8 | inferred_complete_timeline |
| `Action_None` | 48 | 76 | 29 | inferred_complete_timeline |
| `Action_None` | 78 | 208 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 41 | 19 | inferred_complete_timeline |
| `Action_None` | 49 | 58 | 10 | inferred_complete_timeline |
| `Action_None` | 62 | 67 | 6 | inferred_complete_timeline |
| `Action_None` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 117 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 31 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 31 | 9 | inferred_complete_timeline |
| `Action_None` | 37 | 46 | 10 | inferred_complete_timeline |
| `Action_None` | 55 | 58 | 4 | inferred_complete_timeline |
| `Action_None` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_None` | 69 | 91 | 23 | inferred_complete_timeline |
| `Action_None` | 93 | 210 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 31 | 9 | inferred_complete_timeline |
| `Action_None` | 40 | 43 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 132 | 110 | inferred_complete_timeline |
| `Action_None` | 135 | 179 | 45 | inferred_complete_timeline |
| `Action_None` | 182 | 187 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 106 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 74 | 52 | inferred_complete_timeline |
| `Action_None` | 83 | 88 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 111 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 136 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 183 | 161 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 49–99 | 17 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 65–142 | 42 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 67–210 | 142 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 104–210 | 100 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 110–178 | 68 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 133–209 | 68 | 4 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 135–210 | 76 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 142–196 | 11 | 4 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 149–208 | 34 | 5 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 149–158 | 10 | 1 | Undefined position; Undefined team |
| `33` | `34` | Position_Unknown | Team_Unknown | 168–210 | 43 | 1 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 179–210 | 32 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `1` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '0' has invalid range: start=75, end=72. Clamping end to start.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [23–34], lower_priority='Action_ZoneBlock' annotated_start=26, effective_Action_ZoneBlock_start=35.
- ⚠️ Action 'Action_Keep' range [52-72] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-106] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-136] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-183] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-58] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-47] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-93] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-179] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-45] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-83] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-195] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-58] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-107] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [23-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-67] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-45] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-31] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-30] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-44] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-76] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-208] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-58] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-69] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-92] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-210] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-173] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-172] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-193] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '35' has 1 frames without a visible bounding box.
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

</details>