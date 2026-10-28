# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_31`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_31/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 126 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [63–78], lower_priority='Action_PassBlock' annotated_start=66, effective_Action_PassBlock_start=79.
> - Action 'Action_None' range [63-115] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-299] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [63-292] for track '2' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [63-294] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-126] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-184] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-240] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-199] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-264] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-286] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-103] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-191] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-198] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-264] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-297] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-299] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [63-158] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-166] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-280] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-112] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [156-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [168-183] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [186-199] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [203-204] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [79-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-153] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-266] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-153] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-203] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-238] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-266] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-219] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-93] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-80] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [84-153] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-233] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-263] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-281] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-288] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-96] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-154] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-242] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-257] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-270] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-282] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-183] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-255] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-264] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-294] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-141] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-265] for track '27' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-299] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-198] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-299] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-238] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-277] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-267] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '37' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.