# Play-Annotation-Generator Annotation Review — BootPass_103

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_103`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 539
- **Player Tracks:** 80
- **Ball Tracks:** 0
- **Action Segments:** 180
- **Validation Warnings:** 333
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 1
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 5
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 179
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | Team_Unknown | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `18` | `17` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `18` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `13` | `13` | 65 | END | 65 | 65 |
| ❌ MISSING SEGMENT | `Action_FakeHandoff` | Position_Unknown | `13` | `13` | 78 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | `13` | `13` | 96 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_RunFlatRoute` | Position_Unknown | `18` | `17` | 101 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `13` | `13` | 128 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | `18` | `17` | 150 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

*(No offensive player tracks)*

</details>

<details>
<summary><strong>Defense</strong></summary>

*(No defensive player tracks)*

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–77 | 78 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–77 | 78 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–77 | 78 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–77 | 77 | 2 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–55 | 56 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–87 | 88 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–16 | 17 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–77 | 78 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–150 | 57 | 6 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–87 | 88 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 2–68 | 63 | 4 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 3–77 | 48 | 3 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 3–77 | 75 | 1 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 8–77 | 70 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 29–77 | 42 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 59–77 | 12 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 62–76 | 15 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 78–87 | 10 | 1 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 78–86 | 9 | 1 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 111–116 | 6 | 1 | Undefined position; Undefined team |
| `33` | `34` | Position_Unknown | Team_Unknown | 111–149 | 34 | 4 | Undefined position; Undefined team |
| `34` | `35` | Position_Unknown | Team_Unknown | 111–165 | 19 | 4 | Undefined position; Undefined team |
| `35` | `36` | Position_Unknown | Team_Unknown | 118–160 | 43 | 1 | Undefined position; Undefined team |
| `36` | `37` | Position_Unknown | Team_Unknown | 218–539 | 313 | 4 | Undefined position; Undefined team |
| `37` | `38` | Position_Unknown | Team_Unknown | 218–539 | 285 | 4 | Undefined position; Undefined team |
| `38` | `39` | Position_Unknown | Team_Unknown | 218–539 | 319 | 3 | Undefined position; Undefined team |
| `39` | `40` | Position_Unknown | Team_Unknown | 218–378 | 149 | 4 | Undefined position; Undefined team |
| `40` | `41` | Position_Unknown | Team_Unknown | 218–467 | 155 | 4 | Undefined position; Undefined team |
| `41` | `42` | Position_Unknown | Team_Unknown | 218–539 | 256 | 11 | Undefined position; Undefined team |
| `42` | `43` | Position_Unknown | Team_Unknown | 218–457 | 218 | 9 | Undefined position; Undefined team |
| `43` | `44` | Position_Unknown | Team_Unknown | 218–503 | 286 | 1 | Undefined position; Undefined team |
| `44` | `45` | Position_Unknown | Team_Unknown | 218–539 | 314 | 3 | Undefined position; Undefined team |
| `45` | `46` | Position_Unknown | Team_Unknown | 218–539 | 302 | 2 | Undefined position; Undefined team |
| `46` | `47` | Position_Unknown | Team_Unknown | 218–334 | 117 | 1 | Undefined position; Undefined team |
| `47` | `48` | Position_Unknown | Team_Unknown | 218–531 | 303 | 4 | Undefined position; Undefined team |
| `48` | `49` | Position_Unknown | Team_Unknown | 218–539 | 322 | 1 | Undefined position; Undefined team |
| `49` | `50` | Position_Unknown | Team_Unknown | 218–468 | 244 | 4 | Undefined position; Undefined team |
| `50` | `51` | Position_Unknown | Team_Unknown | 218–378 | 147 | 6 | Undefined position; Undefined team |
| `51` | `52` | Position_Unknown | Team_Unknown | 218–531 | 314 | 1 | Undefined position; Undefined team |
| `52` | `53` | Position_Unknown | Team_Unknown | 218–506 | 289 | 1 | Undefined position; Undefined team |
| `53` | `54` | Position_Unknown | Team_Unknown | 218–539 | 282 | 5 | Undefined position; Undefined team |
| `54` | `55` | Position_Unknown | Team_Unknown | 218–248 | 25 | 3 | Undefined position; Undefined team |
| `55` | `56` | Position_Unknown | Team_Unknown | 218–539 | 322 | 1 | Undefined position; Undefined team |
| `56` | `57` | Position_Unknown | Team_Unknown | 218–364 | 147 | 1 | Undefined position; Undefined team |
| `57` | `58` | Position_Unknown | Team_Unknown | 218–388 | 171 | 1 | Undefined position; Undefined team |
| `58` | `59` | Position_Unknown | Team_Unknown | 218–333 | 116 | 1 | Undefined position; Undefined team |
| `59` | `63` | Position_Unknown | Team_Unknown | 361–362 | 2 | 1 | Undefined position; Undefined team |
| `60` | `64` | Position_Unknown | Team_Unknown | 363–539 | 177 | 1 | Undefined position; Undefined team |
| `61` | `65` | Position_Unknown | Team_Unknown | 385–524 | 140 | 1 | Undefined position; Undefined team |
| `62` | `69` | Position_Unknown | Team_Unknown | 397–539 | 134 | 5 | Undefined position; Undefined team |
| `63` | `71` | Position_Unknown | Team_Unknown | 399–539 | 141 | 1 | Undefined position; Undefined team |
| `64` | `73` | Position_Unknown | Team_Unknown | 410–539 | 126 | 2 | Undefined position; Undefined team |
| `65` | `74` | Position_Unknown | Team_Unknown | 412–539 | 103 | 6 | Undefined position; Undefined team |
| `66` | `75` | Position_Unknown | Team_Unknown | 414–423 | 6 | 2 | Undefined position; Undefined team |
| `67` | `77` | Position_Unknown | Team_Unknown | 419–421 | 3 | 1 | Undefined position; Undefined team |
| `68` | `78` | Position_Unknown | Team_Unknown | 421–444 | 24 | 1 | Undefined position; Undefined team |
| `69` | `79` | Position_Unknown | Team_Unknown | 433–539 | 107 | 1 | Undefined position; Undefined team |
| `70` | `80` | Position_Unknown | Team_Unknown | 434–436 | 3 | 1 | Undefined position; Undefined team |
| `71` | `81` | Position_Unknown | Team_Unknown | 435–537 | 85 | 6 | Undefined position; Undefined team |
| `72` | `82` | Position_Unknown | Team_Unknown | 436–539 | 104 | 1 | Undefined position; Undefined team |
| `73` | `84` | Position_Unknown | Team_Unknown | 461–539 | 34 | 8 | Undefined position; Undefined team |
| `74` | `85` | Position_Unknown | Team_Unknown | 470–539 | 70 | 1 | Undefined position; Undefined team |
| `75` | `86` | Position_Unknown | Team_Unknown | 489–493 | 5 | 1 | Undefined position; Undefined team |
| `76` | `87` | Position_Unknown | Team_Unknown | 501–523 | 23 | 1 | Undefined position; Undefined team |
| `77` | `88` | Position_Unknown | Team_Unknown | 503–533 | 26 | 3 | Undefined position; Undefined team |
| `78` | `90` | Position_Unknown | Team_Unknown | 514–516 | 3 | 1 | Undefined position; Undefined team |
| `79` | `94` | Position_Unknown | Team_Unknown | 523–539 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_FakeHandoff` on target `13` (Position_Unknown)
- ❌ Missing segment for action `Action_BootAway` on target `13` (Position_Unknown)
- ❌ Missing segment for action `Action_RunFlatRoute` on target `18` (Position_Unknown)
- ❌ Missing segment for action `Action_ThrowPass` on target `13` (Position_Unknown)
- ❌ Missing segment for action `Action_SecureCatch` on target `18` (Position_Unknown)

### Track Identity Issues

- ⚠️ 80 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 80 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 58 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 160 |
| Missing visible bounding boxes during action | 166 |
| Track-related warning | 5 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_FakeHandoff' for track '13' has invalid range: start=78, end=77. Clamping end to start.
- ⚠️ Segment 'Action_BootAway' for track '13' has invalid range: start=96, end=77. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '13' has invalid range: start=128, end=77. Clamping end to start.
- ⚠️ Segment 'Action_RunFlatRoute' for track '17' has invalid range: start=101, end=87. Clamping end to start.
- ⚠️ Segment 'Action_SecureCatch' for track '17' has invalid range: start=150, end=87. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-77] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-58] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-146] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-46] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-62] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-32] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-77] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-76] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-87] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-86] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-116] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-128] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-131] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-143] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-149] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-125] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-165] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-160] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-341] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-366] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-382] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-539] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-477] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [479-480] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-489] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-366] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-477] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [480-539] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-339] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-358] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-363] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-378] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-363] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-373] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-378] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [465-467] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-341] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-351] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-354] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-362] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-379] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-382] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-390] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-420] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-426] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-431] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-343] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-366] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-373] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-378] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-400] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-418] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-426] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-452] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-457] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-503] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-386] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-396] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-502] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-334] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-386] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-515] for track '47' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [517-522] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [525-531] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-365] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-436] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-465] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-468] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-331] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-334] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-339] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-362] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-373] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-378] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-531] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-506] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-342] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-363] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-378] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-412] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-539] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-230] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-243] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-248] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-364] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-388] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-333] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-362] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-524] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-399] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-422] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-426] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-438] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-539] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-413] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-539] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-413] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-418] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-433] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-489] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [492-493] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-415] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-423] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-421] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-444] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-539] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-436] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-450] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-457] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-489] for track '71' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [493-511] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [517-528] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [535-537] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-539] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-469] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-478] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [480-481] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [498-503] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [511-512] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [519-524] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [530-531] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [489-493] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-523] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [503-513] for track '77' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [518-525] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [527-533] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [514-516] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [523-525] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.

</details>