# Play-Annotation-Generator Annotation Review — BootPass_86

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_86`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 48
- **Ball Tracks:** 1
- **Action Segments:** 131
- **Validation Warnings:** 215
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 5
- **Exact Matches:** 3
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 128
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `12` | `12` |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | Team_Unknown | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `12` | `12` | 62 | END | 62 | 62 |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | `12` | `12` | 65 | START | 65 | 81 |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | `12` | `12` | 89 | START | N/A | N/A |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `9` | `9` | 108 | START | 108 | 118 |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–59 | 60 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–299 | 296 | 3 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–153 | 127 | 3 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–299 | 292 | 5 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–299 | 298 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–299 | 298 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–299 | 295 | 3 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–123 | 123 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–286 | 272 | 6 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–125 | 122 | 5 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–87 | 86 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–145 | 113 | 4 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–81 | 82 | 4 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–299 | 270 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–85 | 86 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–119 | 82 | 6 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–79 | 78 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–110 | 108 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 3–195 | 171 | 8 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 78–299 | 165 | 9 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 80–299 | 219 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 88–299 | 212 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 90–93 | 4 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 95–299 | 205 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 128–299 | 171 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 128–299 | 168 | 5 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 132–145 | 14 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 132–299 | 160 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 143–145 | 3 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 143–259 | 96 | 6 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 145–299 | 138 | 5 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 148–299 | 152 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 149–299 | 148 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 155–158 | 4 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 161–179 | 8 | 2 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 179–299 | 103 | 5 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 181–299 | 119 | 1 | Undefined position; Undefined team |
| `39` | `43` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `40` | `44` | Position_Unknown | Team_Unknown | 192–193 | 2 | 1 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 197–199 | 3 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 201–203 | 3 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 202–216 | 15 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 210–299 | 79 | 3 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 246–299 | 49 | 3 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 253–266 | 14 | 1 | Undefined position; Undefined team |
| `47` | `56` | Position_Unknown | Team_Unknown | 289–290 | 2 | 1 | Undefined position; Undefined team |
| `48` | `57` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | 0 | 46 | 47 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BootAway` on target `12` (Position_Unknown)

### Track Identity Issues

- ⚠️ 48 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 48 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 56 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 96 |
| Missing visible bounding boxes during action | 116 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_BootAway' for track '12' has invalid range: start=89, end=81. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-115] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-299] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-132] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-219] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-232] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-186] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [65-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-299] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-78] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-51] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-58] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-153] for track '19' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-184] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-195] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-92] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-233] for track '20' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-250] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-275] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-287] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-138] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-93] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-166] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-225] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-296] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-145] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-142] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-256] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-299] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-145] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-216] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-234] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-238] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-244] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-238] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-243] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-255] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-267] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-299] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-262] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-158] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-164] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-179] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-212] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-223] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-260] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-278] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-299] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-188] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-199] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-203] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-216] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-224] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-299] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-249] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-266] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-299] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-266] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-290] for track '47' has 1 frames without a visible bounding box.
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

</details>