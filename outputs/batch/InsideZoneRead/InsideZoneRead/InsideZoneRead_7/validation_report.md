# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_7`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_7/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 50 |
| Player Tracks | 50 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 205 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [28–42], lower_priority='Action_ZoneBlock' annotated_start=30, effective_Action_ZoneBlock_start=43.
> - Segment 'Action_BallCarry' for track '21' has invalid range: start=65, end=47. Clamping end to start.
> - Action 'Action_None' range [28-119] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-245] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-284] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-58] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-177] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-227] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-251] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [28-55] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-158] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-214] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-101] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [111-123] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-162] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-211] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [28-42] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-71] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-151] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-172] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-202] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-216] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [225-232] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-260] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [262-270] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-284] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-203] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [205-224] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-71] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [28-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-43] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-67] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-244] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-47] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-55] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-71] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-99] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [100-166] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [232-238] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [240-281] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [285-295] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-45] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-47] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-67] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-71] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-58] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-73] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-23] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-56] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-170] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-188] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-198] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-207] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-73] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-80] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-157] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-187] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-234] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-75] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-122] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-129] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-125] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-151] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-209] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-266] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [278-294] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-124] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-151] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-214] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-288] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [290-299] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-153] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-152] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-175] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-204] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-299] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [136-299] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-149] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-187] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-213] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-229] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-286] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-213] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-299] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-214] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-233] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-258] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-266] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-252] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-291] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-252] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-284] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-298] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-284] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-295] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-284] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-293] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-299] for track '49' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.