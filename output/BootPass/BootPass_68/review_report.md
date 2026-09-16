# Play-Annotation-Generator Annotation Review — BootPass_68

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_68`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 216
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 4
- **Exact Matches:** 1
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 113
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | Team_Unknown | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `15` | `15` | 40 | END | 40 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | `15` | `15` | 50 | START | 50 | 59 |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | `15` | `15` | 78 | START | N/A | N/A |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 5–133 | 127 | 2 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 5–385 | 375 | 4 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 5–76 | 72 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 5–187 | 135 | 5 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 5–108 | 104 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 5–94 | 90 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 5–105 | 101 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 5–172 | 165 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 5–142 | 103 | 4 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 5–118 | 114 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 5–82 | 30 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 5–210 | 203 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 5–290 | 207 | 9 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 5–141 | 122 | 5 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 5–334 | 245 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 5–65 | 57 | 5 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 5–55 | 51 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 5–192 | 182 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 16–48 | 28 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 25–81 | 36 | 5 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 42–61 | 20 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 55–92 | 38 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 61–102 | 38 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 65–67 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 74–108 | 35 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 80–99 | 20 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 89–123 | 35 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 92–140 | 40 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 105–127 | 23 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 111–138 | 23 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 111–162 | 52 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 125–128 | 4 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 126–256 | 126 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 140–273 | 134 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 143–148 | 6 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 144–300 | 152 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 145–153 | 9 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 146–409 | 262 | 2 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 161–167 | 7 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 163–419 | 257 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 179–338 | 121 | 8 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 189–199 | 4 | 2 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 284–294 | 11 | 1 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 292–325 | 28 | 4 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 296–419 | 123 | 2 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 303–419 | 117 | 1 | Undefined position; Undefined team |
| `47` | `69` | Position_Unknown | Team_Unknown | 312–419 | 108 | 1 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 337–419 | 83 | 1 | Undefined position; Undefined team |
| `49` | `72` | Position_Unknown | Team_Unknown | 368–419 | 52 | 1 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 390–395 | 6 | 1 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 396–419 | 21 | 3 | Undefined position; Undefined team |
| `52` | `77` | Position_Unknown | Team_Unknown | 415–419 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `15` (2 segments found)
- ❌ Missing segment for action `Action_BootAway` on target `15` (Position_Unknown)

### Track Identity Issues

- ⚠️ 53 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 53 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 5 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 106 |
| Missing visible bounding boxes during action | 107 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_BootAway' for track '15' has invalid range: start=78, end=65. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [5-102] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-294] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-377] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-385] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-76] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-33] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-51] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-66] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-187] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-94] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-105] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-172] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-99] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-122] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-142] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-20] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-117] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-51] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-268] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-279] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-283] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-290] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-125] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-243] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-334] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [50-59] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [64-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-55] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-107] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-192] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-31] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-48] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-37] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-51] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-70] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-61] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-74] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-67] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-108] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-99] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-117] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-130] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-127] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-118] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-123] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-138] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-162] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-128] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-202] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-256] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-273] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-148] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-286] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-300] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-153] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-200] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-409] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-167] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-419] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-192] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-196] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-206] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-221] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-233] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-323] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-338] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-294] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-298] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-315] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-325] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-328] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-395] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-399] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-404] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-419] for track '51' has 2 frames without a visible bounding box.
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

</details>