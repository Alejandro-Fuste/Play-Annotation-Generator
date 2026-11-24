# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_367`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_367/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 118 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_None' range [183-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-305] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-258] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-201] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-252] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-319] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [186-248] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-275] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-281] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-305] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-226] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-234] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-256] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-305] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-319] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-219] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-250] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-260] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [186-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-21] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-30] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-114] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-206] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [222-250] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [256-273] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [282-284] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [286-290] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [201-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [218-237] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-271] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-35] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-80] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-96] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-224] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-258] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-270] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-288] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-300] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-307] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-318] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-249] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-275] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-300] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-310] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-316] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-290] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-323] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-295] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-306] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.