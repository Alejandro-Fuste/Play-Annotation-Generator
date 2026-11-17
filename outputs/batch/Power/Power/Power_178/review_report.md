# Play-Annotation-Generator Annotation Review — Power_178

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_178`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 39
- **Validation Warnings:** 44
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 27
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `0` | `Group` | 3 | START | 3 | 310 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 3 | START | 3 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 3 | START | 3 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 3 | START | 3 | 252 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 3 | START | 3 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 3 | START | 3 | 111 |
| ✅ EXACT | `Action_DownBlock` | C | `11` | `11` | 112 | START | 112 | 152 |
| ✅ EXACT | `Action_DownBlock` | LT | `9` | `9` | 112 | START | 112 | 152 |
| ✅ EXACT | `Action_PullBlock` | RG | `4` | `4` | 112 | START | 112 | 152 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 3–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 310 | 308 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 322 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 3–249
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 111 | 109 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 152 | 41 | inferred_complete_timeline |
| `Action_None` | 153 | 233 | 81 | inferred_complete_timeline |
| `Action_None` | 236 | 249 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–260
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 172 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 260 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 3–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 111 | 109 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 152 | 41 | inferred_complete_timeline |
| `Action_None` | 153 | 329 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 3–294
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 111 | 109 | inferred_complete_timeline |
| `Action_PullBlock` | 112 | 152 | 41 | inferred_complete_timeline |
| `Action_None` | 153 | 291 | 139 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 3–252
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 252 | 250 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 173 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 329 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–245
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 245 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 3–267
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 124 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 213 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 267 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 3–261
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 261 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 319 | 317 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 329 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–8
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–170
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 170 | 168 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | Position_Unknown | Team_Unknown | 92–183 | 92 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 106–329 | 220 | 2 | Undefined position; Undefined team |
| `16` | `23` | Position_Unknown | Team_Unknown | 172–175 | 4 | 1 | Undefined position; Undefined team |
| `17` | `26` | Position_Unknown | Team_Unknown | 187–329 | 143 | 1 | Undefined position; Undefined team |
| `18` | `27` | Position_Unknown | Team_Unknown | 221–306 | 86 | 1 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 256–329 | 74 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 272–278 | 7 | 1 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 278–329 | 52 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 288–329 | 42 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 24 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 358: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [3-310] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-322] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-172] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-260] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-124] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-213] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-267] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-252] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-291] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-245] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-319] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-261] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-233] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-249] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [112-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-170] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-8] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-183] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-314] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-306] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-278] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.

</details>