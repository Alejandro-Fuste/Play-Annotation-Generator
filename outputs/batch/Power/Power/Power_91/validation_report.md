# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_91`
- **Input XML**: `outputs/batch/Power/Power/Power_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 184: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [16-117] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-329] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-205] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-329] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-215] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-234] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-308] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-200] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-188] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-190] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-297] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-318] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-323] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-329] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-326] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-237] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-324] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-329] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-249] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-179] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-301] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-321] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-327] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [157-173] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [189-200] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-252] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-184] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-207] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-245] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-207] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-219] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-280] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-284] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-314] for track '29' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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