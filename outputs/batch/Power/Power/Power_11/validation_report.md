# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_11`
- **Input XML**: `outputs/batch/Power/Power/Power_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 38 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 24: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [8-232] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-247] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-251] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-269] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-211] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-214] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-254] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-226] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [150-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [169-186] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-231] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '25' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.