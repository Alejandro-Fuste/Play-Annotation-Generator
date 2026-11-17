# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_187`
- **Input XML**: `outputs/batch/Power/Power/Power_187/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-259] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [156-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-295] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-291] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [156-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-289] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-80] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-87] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-152] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-276] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-280] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-10] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-159] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-193] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-74] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-148] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-284] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-201] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-196] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-275] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-297] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-275] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-298] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-211] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-218] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-278] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-291] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-297] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-259] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.