# Play-Annotation-Generator Annotation Review — OutAndUp_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_33`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 103
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB1 | offense | `15` | `15` |
| ✅ EXACT | `Action_SellOut` | Position_Unknown | Team_Unknown | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | Position_Unknown | Team_Unknown | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB1 | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | `0` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `15` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 23 | START | 23 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `11` | `11` | 26 | START | 26 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 26 | START | 27 | 121 |
| ✅ EXACT | `Action_PassBlock` | LT | `19` | `19` | 26 | START | 26 | 34 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 26 | START | 26 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 26 | START | 26 | 211 |
| ✅ EXACT | `Action_SnapReceive` | QB1 | `15` | `15` | 26 | END | 23 | 26 |
| ✅ EXACT | `Action_SellOut` | Position_Unknown | `12` | `12` | 87 | START | 87 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | Position_Unknown | `12` | `12` | 117 | START | 117 | 127 |
| ✅ EXACT | `Action_ThrowPass` | QB1 | `15` | `15` | 128 | START | 128 | 139 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 26 | 4 | inferred_complete_timeline |
| `Action_None` | 27 | 127 | 101 | inferred_complete_timeline |
| `Action_ThrowPass` | 128 | 139 | 12 | inferred_complete_timeline |
| `Action_None` | 140 | 209 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>QB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 86 | 64 | inferred_complete_timeline |
| `Action_None` | 90 | 92 | 3 | inferred_complete_timeline |
| `Action_None` | 94 | 242 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 104 | 82 | inferred_complete_timeline |
| `Action_None` | 106 | 216 | 111 | inferred_complete_timeline |
| `Action_None` | 219 | 269 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 225 | 203 | inferred_complete_timeline |
| `Action_None` | 232 | 250 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 44 | 22 | inferred_complete_timeline |
| `Action_None` | 46 | 71 | 26 | inferred_complete_timeline |
| `Action_None` | 79 | 86 | 8 | inferred_complete_timeline |
| `Action_None` | 90 | 97 | 8 | inferred_complete_timeline |
| `Action_None` | 99 | 136 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 34 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 147 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 23 | 26 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 121 | 95 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 232 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 211 | 186 | inferred_complete_timeline |
| `Action_PassBlock` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 222 | 223 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 114 | 89 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 184 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 42 | 20 | inferred_complete_timeline |
| `Action_None` | 48 | 130 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 156 | 134 | inferred_complete_timeline |
| `Action_None` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_None` | 165 | 231 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 148 | 126 | inferred_complete_timeline |
| `Action_None` | 168 | 215 | 48 | inferred_complete_timeline |
| `Action_None` | 218 | 220 | 3 | inferred_complete_timeline |
| `Action_None` | 222 | 269 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 221 | 199 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |
| `Action_None` | 241 | 244 | 4 | inferred_complete_timeline |
| `Action_None` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 91 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 61 | 39 | inferred_complete_timeline |
| `Action_None` | 65 | 134 | 70 | inferred_complete_timeline |
| `Action_None` | 138 | 228 | 91 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 180 | 158 | inferred_complete_timeline |
| `Action_None` | 184 | 195 | 12 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 150 | 128 | inferred_complete_timeline |
| `Action_None` | 152 | 180 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 149 | 127 | inferred_complete_timeline |
| `Action_None` | 154 | 161 | 8 | inferred_complete_timeline |
| `Action_None` | 163 | 196 | 34 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 206 | 5 | inferred_complete_timeline |
| `Action_None` | 226 | 230 | 5 | inferred_complete_timeline |
| `Action_None` | 232 | 239 | 8 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 90 | 68 | inferred_complete_timeline |
| `Action_None` | 96 | 105 | 10 | inferred_complete_timeline |
| `Action_None` | 107 | 117 | 11 | inferred_complete_timeline |
| `Action_None` | 130 | 132 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–215 | 215 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 57–58 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 60–61 | 2 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 64–241 | 178 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 103–228 | 120 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 160–245 | 86 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 162–254 | 79 | 7 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 163–224 | 62 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 168–226 | 45 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 181–236 | 56 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 189–267 | 46 | 5 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 192–218 | 8 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 206–210 | 5 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 238–269 | 19 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 249–269 | 21 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 252–269 | 12 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 91 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 36: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [23–26], lower_priority='Action_PassBlock' annotated_start=26, effective_Action_PassBlock_start=27.
- ⚠️ Action 'Action_None' range [23-86] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-215] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-90] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-105] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-117] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-216] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-225] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-149] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-196] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-221] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-180] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-195] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-61] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-228] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [117-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [117-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [129-215] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-42] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-130] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-231] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-209] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-71] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-86] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-232] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-147] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-211] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [214-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [222-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-241] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-191] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-202] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-226] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-243] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-254] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-224] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-236] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-245] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-243] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>