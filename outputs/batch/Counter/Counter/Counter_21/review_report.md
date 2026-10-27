# Play-Annotation-Generator Annotation Review — Counter_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_21`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `4` | `3` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB1 | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | DE1 | defense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB2 | offense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_BallCarry` | RB1 | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `12` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `17` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 122 |
| ✅ EXACT | `Action_BallSnap` | C | `4` | `3` | 123 | START | 123 | 137 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB1 | `12` | `11` | 129 | START | 129 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `14` | `13` | 131 | START | 131 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | `18` | `17` | 131 | START | 131 | 225 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `4` | `3` | 131 | START | 138 | 143 |
| ✅ EXACT | `Action_PullBlock` | DE1 | `2` | `1` | 131 | START | 131 | 243 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB2 | `17` | `16` | 131 | START | 131 | 235 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `22` | `21` | 137 | END | 123 | 137 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `22` | `21` | 160 | START | 160 | 174 |
| ✅ EXACT | `Action_BallCarry` | RB1 | `12` | `11` | 175 | START | 175 | 280 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 243 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 129 | 174 | 46 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 280 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 131 | 235 | 105 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 238 | 243 | 6 | inferred_complete_timeline |
| `Action_None` | 244 | 299 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–295
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 295 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 225 | 95 | inferred_complete_timeline |
| `Action_DownBlock` | 235 | 243 | 9 | inferred_complete_timeline |
| `Action_None` | 244 | 299 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 233 | 111 | inferred_complete_timeline |
| `Action_None` | 235 | 242 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_BallSnap` | 123 | 137 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 138 | 143 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 156 | 161 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 163 | 243 | 81 | inferred_complete_timeline |
| `Action_None` | 244 | 299 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 144 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 157 | 208 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 213 | 243 | 31 | inferred_complete_timeline |
| `Action_None` | 244 | 299 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 147 | 25 | inferred_complete_timeline |
| `Action_None` | 170 | 181 | 12 | inferred_complete_timeline |
| `Action_None` | 184 | 187 | 4 | inferred_complete_timeline |
| `Action_None` | 202 | 208 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PullBlock` | 131 | 243 | 113 | inferred_complete_timeline |
| `Action_None` | 244 | 299 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 202 | 80 | inferred_complete_timeline |
| `Action_None` | 210 | 299 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 158 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 173 | 51 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 206 | 20 | inferred_complete_timeline |
| `Action_None` | 208 | 261 | 54 | inferred_complete_timeline |
| `Action_None` | 264 | 299 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 222 | 100 | inferred_complete_timeline |
| `Action_None` | 225 | 299 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 241 | 119 | inferred_complete_timeline |
| `Action_None` | 243 | 299 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 237 | 115 | inferred_complete_timeline |
| `Action_None` | 239 | 299 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 279 | 157 | inferred_complete_timeline |
| `Action_None` | 282 | 284 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 2–237 | 236 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 142–299 | 152 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 173–246 | 74 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 252–299 | 48 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 266–299 | 34 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 289–299 | 11 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '1' (DE1) duration 113 frames exceeds threshold 90 frames [start=131, end=243].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (C) duration 113 frames exceeds threshold 90 frames [start=131, end=243].
- ⚠️ Resolved action overlap for track '3' (C): higher_priority='Action_BallSnap' [123–137], lower_priority='Action_DownBlock' annotated_start=131, effective_Action_DownBlock_start=138.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (RG) duration 113 frames exceeds threshold 90 frames [start=131, end=243].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (TE) duration 113 frames exceeds threshold 90 frames [start=131, end=243].
- ⚠️ Action 'Action_DownBlock' range [138-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [156-161] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [163-243] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-299] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-222] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-295] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-279] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [175-280] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-241] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [148-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-208] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-206] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-261] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [131-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-225] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-242] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-222] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-234] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-246] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '26' has 1 frames without a visible bounding box.
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