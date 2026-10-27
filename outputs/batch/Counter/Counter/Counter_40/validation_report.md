# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_40`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_40/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PullBlock' range [228-279] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-325] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [228-274] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-365] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-341] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [344-389] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-346] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-372] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-292] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-344] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-389] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [228-265] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-371] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [373-374] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [264-369] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-270] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-327] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-333] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-342] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-389] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-333] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-342] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-349] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [353-357] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-382] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-351] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-355] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-389] for track '30' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.