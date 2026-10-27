# Play-Annotation-Generator Annotation Review — Dagger_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_6`
- **Frame Range:** 0 to 448 (449 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 448
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 76
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_BreakInside` | WR1 | offense | `14` | `14` |
| ✅ EXACT | `Action_ClearToEdge` | WR2 | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 75 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 70 | START | 70 | 76 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `16` | `16` | 73 | START | 77 | 169 |
| ✅ EXACT | `Action_PassBlock` | RT | `18` | `18` | 73 | START | 73 | 448 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `19` | `19` | 73 | START | 73 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 73 | START | 73 | 190 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 73 | START | 73 | 288 |
| ✅ EXACT | `Action_BreakInside` | WR1 | `14` | `14` | 76 | START | 76 | 246 |
| ✅ EXACT | `Action_ClearToEdge` | WR2 | `9` | `9` | 76 | START | 76 | 198 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 76 | END | 70 | 76 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 189 | START | 189 | 198 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_SnapReceive` | 70 | 76 | 7 | inferred_complete_timeline |
| `Action_None` | 77 | 188 | 112 | inferred_complete_timeline |
| `Action_ThrowPass` | 189 | 198 | 10 | inferred_complete_timeline |
| `Action_None` | 199 | 448 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 448 | 379 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_BreakInside` | 76 | 246 | 171 | inferred_complete_timeline |
| `Action_None` | 247 | 375 | 129 | inferred_complete_timeline |
| `Action_None` | 377 | 387 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_ClearToEdge` | 76 | 198 | 123 | inferred_complete_timeline |
| `Action_None` | 199 | 448 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–443
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 383 | 314 | inferred_complete_timeline |
| `Action_None` | 386 | 420 | 35 | inferred_complete_timeline |
| `Action_None` | 423 | 435 | 13 | inferred_complete_timeline |
| `Action_None` | 439 | 443 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 203 | 134 | inferred_complete_timeline |
| `Action_None` | 208 | 448 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 72 | 58 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 160 | 88 | inferred_complete_timeline |
| `Action_PassBlock` | 162 | 165 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 169 | 267 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–363
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 72 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 190 | 118 | inferred_complete_timeline |
| `Action_PassBlock` | 193 | 363 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_BallSnap` | 70 | 76 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 169 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 22 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 72 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 288 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 72 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 448 | 376 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 133 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 69 | 53 | inferred_complete_timeline |
| `Action_None` | 70 | 284 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–376
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 69 | 55 | inferred_complete_timeline |
| `Action_None` | 70 | 376 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 178 | 109 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_None` | 188 | 448 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 448 | 379 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 448 | 379 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 418 | 349 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 448 | 379 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 448 | 379 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 271 | 202 | inferred_complete_timeline |
| `Action_None` | 273 | 286 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–432
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 365 | 296 | inferred_complete_timeline |
| `Action_None` | 370 | 432 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 121–123 | 3 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 155–448 | 294 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 184–390 | 207 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 251–254 | 4 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 255–256 | 2 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 280–448 | 168 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 302–448 | 146 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 305–319 | 15 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 358–405 | 29 | 5 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 388–448 | 61 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 430–448 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `16` (C): Annotated start 73 != Inferred start 77
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 448 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [70–76], lower_priority='Action_PassBlock' annotated_start=73, effective_Action_PassBlock_start=77.
- ⚠️ Action 'Action_None' range [70-383] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-420] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-435] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-443] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-365] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-432] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-271] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-286] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-418] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-448] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-203] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-376] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-448] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-375] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-387] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-169] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-284] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-160] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [162-165] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [169-267] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-190] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [193-363] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-22] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-288] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-390] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-286] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-357] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-319] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-364] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-378] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-405] for track '32' has 1 frames without a visible bounding box.
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

</details>