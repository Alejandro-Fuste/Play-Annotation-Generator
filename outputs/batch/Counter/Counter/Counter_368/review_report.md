# Play-Annotation-Generator Annotation Review — Counter_368

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_368`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 14 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 41 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 42 | START | 42 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 45 | START | 57 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `15` | `14` | 45 | START | 45 | 208 |
| ✅ EXACT | `Action_PullBlock` | RG | `12` | `11` | 45 | START | 45 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `13` | `12` | 45 | START | 45 | 173 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 56 | END | 42 | 56 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 63 | START | 63 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 86 | START | 86 | 177 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 222 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 56 | 15 | inferred_complete_timeline |
| `Action_None` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 63 | 85 | 23 | inferred_complete_timeline |
| `Action_None` | 86 | 176 | 91 | inferred_complete_timeline |
| `Action_None` | 190 | 195 | 6 | inferred_complete_timeline |
| `Action_None` | 197 | 299 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_BallCarry` | 86 | 177 | 92 | inferred_complete_timeline |
| `Action_BallCarry` | 180 | 182 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 44 | 11 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 45 | 173 | 129 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 184 | 204 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 14–212
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 44 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 45 | 208 | 164 | inferred_complete_timeline |
| `Action_DownBlock` | 211 | 212 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 161 | 120 | inferred_complete_timeline |
| `Action_None` | 168 | 170 | 3 | inferred_complete_timeline |
| `Action_None` | 174 | 184 | 11 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 269 | 271 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_BallSnap` | 42 | 56 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 57 | 155 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PullBlock` | 45 | 171 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 187 | 146 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 190 | 149 | inferred_complete_timeline |
| `Action_None` | 217 | 299 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 280 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 193 | 152 | inferred_complete_timeline |
| `Action_None` | 197 | 200 | 4 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 241 | 16 | inferred_complete_timeline |
| `Action_None` | 244 | 253 | 10 | inferred_complete_timeline |
| `Action_None` | 255 | 281 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 191 | 150 | inferred_complete_timeline |
| `Action_None` | 202 | 220 | 19 | inferred_complete_timeline |
| `Action_None` | 243 | 276 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 262 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 230 | 189 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |
| `Action_None` | 238 | 241 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 281 | 240 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 297 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `19` | Position_Unknown | Team_Unknown | 163–277 | 112 | 3 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 183–299 | 117 | 1 | Undefined position; Undefined team |
| `17` | `24` | Position_Unknown | Team_Unknown | 193–299 | 107 | 1 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 194–299 | 101 | 4 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 204–228 | 21 | 3 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 207–228 | 22 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 228–299 | 50 | 2 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 257–299 | 33 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 259–299 | 41 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 261–269 | 7 | 3 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 268–299 | 32 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 270–299 | 30 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 281–299 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '11' (RG) duration 127 frames exceeds threshold 90 frames [start=45, end=171].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (C) duration 111 frames exceeds threshold 90 frames [start=45, end=155].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [42–56], lower_priority='Action_DownBlock' annotated_start=45, effective_Action_DownBlock_start=57.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '14' (LT) duration 168 frames exceeds threshold 90 frames [start=45, end=212].
- ⚠️ Action 'Action_None' range [42-280] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-281] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-161] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-230] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [86-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [180-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-176] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-191] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-276] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-299] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-193] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-241] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-253] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-281] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-262] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [45-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [45-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [184-204] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [57-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [45-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [211-212] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-215] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-271] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-291] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-224] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-247] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-293] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '24' has 1 frames without a visible bounding box.
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