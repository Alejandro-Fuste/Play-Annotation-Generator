# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_158`
- **Input XML**: `outputs/batch/Power/Power/Power_158/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 42 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 317: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 318: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [10-241] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-273] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [151-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-247] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-232] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-265] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-228] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-310] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-39] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-208] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-212] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-235] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-244] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-291] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-354] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-286] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-304] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-337] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-347] for track '26' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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