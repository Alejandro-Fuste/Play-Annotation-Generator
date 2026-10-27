# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_356`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_356/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_DownBlock' range [239-320] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-335] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [239-270] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-331] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-396] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [403-408] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-417] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-335] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-273] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [280-285] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [287-290] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [293-315] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-257] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-281] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-300] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-325] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [239-295] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-349] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-371] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-408] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-316] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [236-247] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-292] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-322] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-419] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-38] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-49] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-94] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-176] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-188] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-232] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [239-261] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [269-271] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-253] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-242] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [262-265] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [270-277] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-316] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-320] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-296] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-304] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-317] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-310] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-317] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-335] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-315] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-355] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-360] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-397] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [341-419] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-358] for track '23' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.