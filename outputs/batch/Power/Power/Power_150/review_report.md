# Play-Annotation-Generator Annotation Review — Power_150

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_150`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 55
- **Validation Warnings:** 61
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 38
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 14 | START | 14 | 425 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 14 | START | 14 | 401 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 14 | START | 14 | 336 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 14 | START | 14 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 14 | START | 14 | 314 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 14 | START | 14 | 401 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 14 | START | 14 | 314 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 14 | START | 14 | 314 |
| ✅ EXACT | `Action_DownBlock` | LG | `3` | `3` | 315 | START | 315 | 347 |
| ✅ EXACT | `Action_DownBlock` | RG | `6` | `6` | 315 | START | 315 | 381 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `8` | `8` | 315 | START | 315 | 320 |

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
- **Visible Frames:** 14–479
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 479 | 466 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 14–448
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 401 | 388 | inferred_complete_timeline |
| `Action_PreSnap` | 439 | 448 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 14–457
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 425 | 412 | inferred_complete_timeline |
| `Action_PreSnap` | 435 | 446 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 455 | 457 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 14–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 401 | 388 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 415 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 420 | 479 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 14–347
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 314 | 301 | inferred_complete_timeline |
| `Action_DownBlock` | 315 | 347 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 14–479
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 336 | 323 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 479 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 14–479
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 314 | 301 | inferred_complete_timeline |
| `Action_DownBlock` | 315 | 381 | 67 | inferred_complete_timeline |
| `Action_None` | 382 | 479 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 14–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 314 | 301 | inferred_complete_timeline |
| `Action_PullBlock` | 315 | 320 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 323 | 381 | 59 | inferred_complete_timeline |
| `Action_None` | 382 | 443 | 62 | inferred_complete_timeline |
| `Action_None` | 445 | 449 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 14–479
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 479 | 466 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 14–479
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 433 | 420 | inferred_complete_timeline |
| `Action_PreSnap` | 450 | 479 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 14–333
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 327 | 314 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 333 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 14–479
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 370 | 357 | inferred_complete_timeline |
| `Action_PreSnap` | 425 | 479 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 14–374
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 374 | 361 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 14–479
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 342 | 329 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 479 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 14–432
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 432 | 419 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 146–441 | 128 | 9 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 337–468 | 132 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 346–479 | 127 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 373–426 | 54 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 376–479 | 104 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 387–479 | 93 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 390–479 | 90 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 405–455 | 51 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 406–479 | 73 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 418–450 | 28 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 477–479 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 38 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [14-425] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-446] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-457] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-433] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [315-347] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-401] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-415] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-479] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-432] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-342] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [315-320] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-443] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-449] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-374] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-401] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-448] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-336] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-327] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-333] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-370] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-479] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-315] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-333] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-367] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-384] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-390] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-396] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-441] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-468] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-398] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-414] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-426] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-455] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-463] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-435] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-450] for track '24' has 3 frames without a visible bounding box.
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

</details>