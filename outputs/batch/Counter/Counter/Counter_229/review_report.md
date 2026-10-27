# Play-Annotation-Generator Annotation Review — Counter_229

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_229`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 97
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
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE2 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | offense | `6` | `5` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 112 |
| ✅ EXACT | `Action_BallSnap` | DE2 | `15` | `14` | 111 | START | 111 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `10` | `9` | 113 | START | 113 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | `15` | `14` | 113 | START | 113 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 113 | START | 113 | 140 |
| ✅ EXACT | `Action_PullBlock` | LG | `22` | `21` | 113 | START | 113 | 199 |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | `6` | `5` | 113 | START | 113 | 246 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `14` | `13` | 123 | START | 123 | 161 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 126 | END | 111 | 126 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `15` | 140 | START | 140 | 161 |
| ✅ EXACT | `Action_BallCarry` | RB | `14` | `13` | 162 | START | 162 | 222 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 246 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_SnapReceive` | 111 | 126 | 16 | inferred_complete_timeline |
| `Action_None` | 127 | 139 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 140 | 161 | 22 | inferred_complete_timeline |
| `Action_None` | 162 | 359 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 123 | 161 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 162 | 222 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 196 | 86 | inferred_complete_timeline |
| `Action_None` | 204 | 242 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 359 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 113 | 246 | 134 | inferred_complete_timeline |
| `Action_None` | 247 | 359 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 158 | 48 | inferred_complete_timeline |
| `Action_None` | 160 | 167 | 8 | inferred_complete_timeline |
| `Action_None` | 171 | 359 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 204 | 94 | inferred_complete_timeline |
| `Action_None` | 208 | 359 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PullBlock` | 113 | 199 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 140 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 145 | 153 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 177 | 211 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 215 | 246 | 32 | inferred_complete_timeline |
| `Action_None` | 247 | 359 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 156 | 44 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 178 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 222 | 246 | 25 | inferred_complete_timeline |
| `Action_None` | 247 | 340 | 94 | inferred_complete_timeline |
| `Action_None` | 343 | 355 | 13 | inferred_complete_timeline |
| `Action_None` | 358 | 359 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 238 | 128 | inferred_complete_timeline |
| `Action_None` | 242 | 249 | 8 | inferred_complete_timeline |
| `Action_None` | 256 | 261 | 6 | inferred_complete_timeline |
| `Action_None` | 263 | 330 | 68 | inferred_complete_timeline |
| `Action_None` | 333 | 359 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_BallSnap` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 122 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 137 | 246 | 110 | inferred_complete_timeline |
| `Action_None` | 247 | 359 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 359 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 146 | 36 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_None` | 163 | 211 | 49 | inferred_complete_timeline |
| `Action_None` | 213 | 359 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 359 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 359 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 303 | 193 | inferred_complete_timeline |
| `Action_None` | 308 | 311 | 4 | inferred_complete_timeline |
| `Action_None` | 315 | 319 | 5 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 359 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 359 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 359 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 239 | 129 | inferred_complete_timeline |
| `Action_None` | 242 | 290 | 49 | inferred_complete_timeline |
| `Action_None` | 296 | 359 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–359 | 330 | 11 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 84–358 | 143 | 14 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 182–359 | 174 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 188–190 | 3 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 190–359 | 168 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 232–340 | 9 | 3 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 251–359 | 106 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 264–271 | 8 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 328–333 | 5 | 2 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 349–350 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 460: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '9' (RT) duration 134 frames exceeds threshold 90 frames [start=113, end=246].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '14' (DE2) duration 134 frames exceeds threshold 90 frames [start=113, end=246].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (RG) duration 134 frames exceeds threshold 90 frames [start=113, end=246].
- ⚠️ Action 'Action_None' range [111-196] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-290] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [158-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-340] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-355] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-249] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-330] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-324] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [162-222] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-303] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-146] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-211] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-359] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [145-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [158-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [177-211] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [113-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-222] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-359] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-301] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-271] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '30' has 1 frames without a visible bounding box.
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

</details>