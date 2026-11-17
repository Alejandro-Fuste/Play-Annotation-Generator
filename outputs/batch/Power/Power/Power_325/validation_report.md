# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_325`
- **Input XML**: `outputs/batch/Power/Power/Power_325/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [5-297] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-245] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-293] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-323] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-248] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-278] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-58] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [195-216] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-297] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-279] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-291] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-307] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-267] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-263] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-223] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-256] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-280] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-321] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-62] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-232] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-242] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-302] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-258] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-329] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-329] for track '30' has 1 frames without a visible bounding box.
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