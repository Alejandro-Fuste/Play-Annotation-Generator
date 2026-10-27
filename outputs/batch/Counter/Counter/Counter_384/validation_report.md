# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_384`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_384/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [142–159], lower_priority='Action_DownBlock' annotated_start=145, effective_Action_DownBlock_start=160.
> - Action 'Action_None' range [142-199] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-219] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-385] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-199] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-213] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-354] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-201] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [145-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [178-185] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [192-197] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-240] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-212] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-389] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [160-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [183-184] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [189-227] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-378] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-215] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-353] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-389] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-173] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-207] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [145-211] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [228-303] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-389] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-306] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-316] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-389] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-389] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-206] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-219] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-362] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-260] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-319] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-310] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-308] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-311] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-336] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-380] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-384] for track '32' has 2 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.