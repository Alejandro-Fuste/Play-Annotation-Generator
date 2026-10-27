# Play-Annotation-Generator Annotation Review — Counter_196

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_196`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | WR2 | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB1 | defense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR2 | offense | `6` | `5` |
| ✅ EXACT | `Action_DownBlock` | DE1 | defense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | OLB1 | defense | `2` | `1` |
| ✅ EXACT | `Action_PullLeadBlock` | LB1 | defense | `11` | `10` |
| ✅ EXACT | `Action_PlaySideFakeStep` | LB1 | defense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | LB1 | defense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `22` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 93 |
| ✅ EXACT | `Action_BallSnap` | WR2 | `6` | `5` | 94 | START | 94 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB1 | `10` | `9` | 97 | START | 97 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR2 | `6` | `5` | 97 | START | 97 | 189 |
| ✅ EXACT | `Action_DownBlock` | DE1 | `7` | `6` | 97 | START | 97 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | OLB1 | `2` | `1` | 97 | START | 97 | 143 |
| ✅ EXACT | `Action_PullLeadBlock` | LB1 | `11` | `10` | 97 | START | 97 | 98 |
| ✅ EXACT | `Action_PlaySideFakeStep` | LB1 | `11` | `10` | 99 | START | 99 | 136 |
| ✅ EXACT | `Action_SnapReceive` | RB | `8` | `7` | 100 | END | 94 | 100 |
| ✅ EXACT | `Action_Handoff` | RB | `8` | `7` | 121 | START | 121 | 136 |
| ✅ EXACT | `Action_BallCarry` | LB1 | `11` | `10` | 137 | START | 137 | 177 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 189 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 164 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_SnapReceive` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_None` | 101 | 120 | 20 | inferred_complete_timeline |
| `Action_Handoff` | 121 | 136 | 16 | inferred_complete_timeline |
| `Action_None` | 137 | 211 | 75 | inferred_complete_timeline |
| `Action_None` | 217 | 269 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 162 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_BallSnap` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 189 | 93 | inferred_complete_timeline |
| `Action_None` | 190 | 258 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 186 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 143 | 50 | inferred_complete_timeline |
| `Action_None` | 149 | 177 | 29 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 219 | 34 | inferred_complete_timeline |
| `Action_None` | 232 | 248 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 151 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 159–166
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 159 | 166 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 168–239
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 168 | 178 | 11 | inferred_complete_timeline |
| `Action_None` | 180 | 187 | 8 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_None` | 200 | 219 | 20 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 138–147
- **Visible Samples:** 10

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 138 | 147 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 189 | 93 | inferred_complete_timeline |
| `Action_None` | 190 | 254 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 152–242
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 152 | 162 | 11 | inferred_complete_timeline |
| `Action_None` | 178 | 242 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 117 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 99 | 136 | 38 | inferred_complete_timeline |
| `Action_BallCarry` | 137 | 177 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 269 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PullBlock` | 97 | 143 | 47 | inferred_complete_timeline |
| `Action_PullBlock` | 151 | 189 | 39 | inferred_complete_timeline |
| `Action_None` | 190 | 221 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `20`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 157–250
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 250 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 145 | 49 | inferred_complete_timeline |
| `Action_DownBlock` | 148 | 189 | 42 | inferred_complete_timeline |
| `Action_None` | 190 | 242 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 120 | 27 | inferred_complete_timeline |
| `Action_None` | 122 | 269 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 114 | 21 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_None` | 131 | 139 | 9 | inferred_complete_timeline |
| `Action_None` | 141 | 254 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 215 | 122 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 181–229 | 49 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 196–269 | 74 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 199–206 | 8 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 219–269 | 48 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 225–239 | 10 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 233–269 | 37 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 243–269 | 27 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '1' (OLB1) duration 93 frames exceeds threshold 90 frames [start=97, end=189].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '5' (WR2) duration 93 frames exceeds threshold 90 frames [start=97, end=189].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '6' (DE1) duration 93 frames exceeds threshold 90 frames [start=97, end=189].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '9' (CB1) duration 93 frames exceeds threshold 90 frames [start=97, end=189].
- ⚠️ Action 'Action_None' range [94-162] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [97-143] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-177] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-219] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-248] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-215] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [97-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-258] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-254] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-211] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [97-145] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-242] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [137-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-254] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-242] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-219] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-261] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-269] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>