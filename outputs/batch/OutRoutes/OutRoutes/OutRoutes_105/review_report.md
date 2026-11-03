# Play-Annotation-Generator Annotation Review — OutRoutes_105

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_105`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 141
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `11` | `11` | 29 | START | 29 | 58 |
| ✅ EXACT | `Action_PassBlock` | RG | `12` | `12` | 29 | START | 29 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 29 | START | 29 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 29 | START | 29 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 29 | START | 29 | 43 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `3` | `3` | 34 | START | 34 | 101 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 34 | END | 34 | 34 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 69 | START | 69 | 79 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `3` | `3` | 102 | START | 102 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `3` | `3` | 110 | START | 110 | 158 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_None` | 35 | 68 | 34 | inferred_complete_timeline |
| `Action_ThrowPass` | 69 | 79 | 11 | inferred_complete_timeline |
| `Action_None` | 80 | 92 | 13 | inferred_complete_timeline |
| `Action_None` | 95 | 99 | 5 | inferred_complete_timeline |
| `Action_None` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_None` | 106 | 132 | 27 | inferred_complete_timeline |
| `Action_None` | 145 | 171 | 27 | inferred_complete_timeline |
| `Action_None` | 173 | 177 | 5 | inferred_complete_timeline |
| `Action_None` | 183 | 239 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_RunOutRoute` | 34 | 101 | 68 | inferred_complete_timeline |
| `Action_SecureCatch` | 102 | 109 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 158 | 49 | inferred_complete_timeline |
| `Action_BallCarry` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 239 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 85 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 117 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 159 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 239 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 158 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 193 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 197 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 239 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 58 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 61 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 37 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 47 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 43 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 48 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 110 | 49 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 136 | 239 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 77 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 115 | 87 | inferred_complete_timeline |
| `Action_PassBlock` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 239 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 58 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 113 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 132 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 239 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 142 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 239 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 142 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 239 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 193 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 204 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–42 | 43 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 54–156 | 103 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 62–239 | 161 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 78–88 | 9 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 80–236 | 111 | 4 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 82–94 | 12 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 85–101 | 10 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 95–100 | 6 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 98–109 | 12 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 101–235 | 46 | 5 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 105–106 | 2 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 137–209 | 56 | 3 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 137–239 | 103 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 155–159 | 5 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 160–239 | 62 | 5 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 169–171 | 3 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 187–196 | 8 | 2 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 198–204 | 5 | 2 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 205–239 | 35 | 1 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 213–219 | 7 | 1 | Undefined position; Undefined team |
| `42` | `50` | Position_Unknown | Team_Unknown | 214–219 | 6 | 1 | Undefined position; Undefined team |
| `43` | `51` | Position_Unknown | Team_Unknown | 216–222 | 7 | 1 | Undefined position; Undefined team |
| `44` | `54` | Position_Unknown | Team_Unknown | 228–236 | 9 | 1 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 91 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-193] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-197] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [160-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-58] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-113] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-132] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-193] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-147] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-58] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-92] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [126-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-37] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-52] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-110] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [130-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [136-239] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-156] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-96] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-83] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-88] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-101] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-202] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-87] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-94] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-91] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-101] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-100] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-109] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-109] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-174] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-219] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-229] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-106] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-147] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-162] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-209] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-159] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-181] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-206] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-211] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-227] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-171] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-190] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-196] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-204] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-239] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-219] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-219] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-222] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-236] for track '44' has 3 frames without a visible bounding box.
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
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.

</details>