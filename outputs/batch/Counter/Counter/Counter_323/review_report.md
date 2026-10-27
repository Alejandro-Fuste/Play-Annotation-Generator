# Play-Annotation-Generator Annotation Review — Counter_323

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_323`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 54
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `20` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 172 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | QB | `13` | `12` | 173 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 176 | START | 176 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 176 | START | 176 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `22` | `21` | 176 | START | 176 | 217 |
| ✅ EXACT | `Action_PullBlock` | LG | `18` | `17` | 176 | START | 176 | 278 |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | `4` | `3` | 176 | START | 176 | 278 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 187 | END | 173 | 187 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 196 | START | 196 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `15` | `14` | 215 | START | 215 | 266 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 278 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_SnapReceive` | 173 | 187 | 15 | inferred_complete_timeline |
| `Action_None` | 188 | 195 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 196 | 214 | 19 | inferred_complete_timeline |
| `Action_None` | 215 | 355 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_BallCarry` | 215 | 266 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 272 | 389 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 344 | 172 | inferred_complete_timeline |
| `Action_None` | 349 | 350 | 2 | inferred_complete_timeline |
| `Action_None` | 352 | 371 | 20 | inferred_complete_timeline |
| `Action_None` | 374 | 389 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 176 | 278 | 103 | inferred_complete_timeline |
| `Action_None` | 279 | 389 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PullBlock` | 176 | 278 | 103 | inferred_complete_timeline |
| `Action_None` | 279 | 389 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_DownBlock` | 176 | 190 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 200 | 205 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 207 | 211 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_DownBlock` | 176 | 205 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_DownBlock` | 176 | 217 | 42 | inferred_complete_timeline |
| `Action_DownBlock` | 219 | 223 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 230 | 233 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 235 | 278 | 44 | inferred_complete_timeline |
| `Action_None` | 279 | 389 | 111 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 225 | 53 | inferred_complete_timeline |
| `Action_None` | 231 | 251 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 302 | 130 | inferred_complete_timeline |
| `Action_None` | 305 | 372 | 68 | inferred_complete_timeline |
| `Action_None` | 378 | 389 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 343 | 171 | inferred_complete_timeline |
| `Action_None` | 350 | 389 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 265 | 93 | inferred_complete_timeline |
| `Action_None` | 267 | 389 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 355 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 252 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 302 | 130 | inferred_complete_timeline |
| `Action_None` | 305 | 374 | 70 | inferred_complete_timeline |
| `Action_None` | 376 | 384 | 9 | inferred_complete_timeline |
| `Action_None` | 387 | 389 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 215–234 | 20 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 239–389 | 150 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 248–389 | 126 | 5 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 253–389 | 137 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 265–389 | 125 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 347–349 | 3 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 373–374 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `13` (QB)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '17' (LG) duration 103 frames exceeds threshold 90 frames [start=176, end=278].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (RT) duration 103 frames exceeds threshold 90 frames [start=176, end=278].
- ⚠️ Action 'Action_None' range [173-344] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-371] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-302] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-372] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-251] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-343] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-355] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-389] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [176-190] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [200-205] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [207-211] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-355] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-265] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [215-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [272-389] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-302] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-374] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-384] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-252] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [176-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [176-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [219-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [230-233] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-234] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-247] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-389] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-389] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '28' has 1 frames without a visible bounding box.
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

</details>