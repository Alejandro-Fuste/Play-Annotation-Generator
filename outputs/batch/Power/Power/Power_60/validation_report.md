# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_60`
- **Input XML**: `outputs/batch/Power/Power/Power_60/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [17-188] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-269] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-299] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [136-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [164-189] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-252] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-278] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-191] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [136-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [152-168] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-230] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-253] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-208] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-259] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-290] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-216] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-146] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-174] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-137] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [136-142] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-165] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-281] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-177] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-257] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-34] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-99] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-212] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-215] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-220] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-290] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-254] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-270] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-286] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-299] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-282] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-297] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-274] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-296] for track '30' has 2 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.