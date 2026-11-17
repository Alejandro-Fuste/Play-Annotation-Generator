# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_9`
- **Input XML**: `outputs/batch/Power/Power/Power_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 45 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [6-211] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-234] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-309] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-327] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-284] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-290] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-302] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-280] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-305] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-312] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-329] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [162-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-219] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-248] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-303] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [162-170] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-208] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-219] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '25' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.