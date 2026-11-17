# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_284`
- **Input XML**: `outputs/batch/Power/Power/Power_284/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 25 |
| Ball Tracks | 2 |
| CSV events parsed | 13 |
| Action Segments inferred | 41 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [20-329] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-379] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-419] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-365] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-403] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [314-331] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-173] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-334] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-202] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-323] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-371] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [314-342] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-392] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-197] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-419] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-348] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-353] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-405] for track '26' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.