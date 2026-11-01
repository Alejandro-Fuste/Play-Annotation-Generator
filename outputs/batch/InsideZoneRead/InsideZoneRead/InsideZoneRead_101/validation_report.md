# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_101`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_101/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 204: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [146–158], lower_priority='Action_ZoneBlock' annotated_start=149, effective_Action_ZoneBlock_start=159.
> - Action 'Action_None' range [146-282] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-292] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-177] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-285] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [309-311] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-252] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-178] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-178] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-215] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [217-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-245] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-229] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-183] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-228] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-271] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-283] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-291] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-258] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-172] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-197] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-226] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-211] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-233] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-251] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-259] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-265] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-281] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-278] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-286] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-260] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-329] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-251] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-316] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-329] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-329] for track '36' has 1 frames without a visible bounding box.
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