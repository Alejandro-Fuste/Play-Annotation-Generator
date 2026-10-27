# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_117`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_117/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '8' (RT) duration 102 frames exceeds threshold 90 frames [start=266, end=367].
> - Validation warning: Action 'Action_DownBlock' for track '11' (C) duration 102 frames exceeds threshold 90 frames [start=266, end=367].
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [264–277], lower_priority='Action_DownBlock' annotated_start=266, effective_Action_DownBlock_start=278.
> - Action 'Action_None' range [264-406] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-342] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-369] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-449] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [310-314] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-289] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-306] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-317] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-333] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [344-370] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-382] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-395] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [418-419] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-449] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-420] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [422-428] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-304] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-340] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-344] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [266-309] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-392] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [264-354] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-371] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-373] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [278-329] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [333-367] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-371] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-391] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [427-439] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [443-444] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-401] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-407] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-446] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [310-421] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-404] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-449] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-306] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [266-346] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-341] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [266-283] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [303-311] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-346] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-437] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-351] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-364] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [366-391] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [394-395] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-449] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-369] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-382] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [384-391] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-395] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-409] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-370] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-391] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [444-447] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [420-427] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-434] for track '29' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.