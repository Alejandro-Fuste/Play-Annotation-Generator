# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_308`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_308/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_None' range [164-240] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-287] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-305] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-154] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-325] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-336] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-348] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-353] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-319] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-349] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-224] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-197] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-250] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-298] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-110] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-359] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-254] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-135] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-153] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-238] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-231] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [139-323] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [325-327] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [340-341] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-128] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-169] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-263] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-293] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-290] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-240] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-248] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-304] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-297] for track '28' has 2 frames without a visible bounding box.
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