# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_173`
- **Input XML**: `outputs/batch/Power/Power/Power_173/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 348: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [3-241] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-284] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-280] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-285] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-227] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-235] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-27] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-159] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-167] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-29] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-13] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-299] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-26] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-14] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-19] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-129] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [130-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [137-170] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [130-175] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-11] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [130-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-11] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-15] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-233] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-216] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-237] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-250] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-259] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-274] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-224] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-299] for track '28' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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