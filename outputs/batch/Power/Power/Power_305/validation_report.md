# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_305`
- **Input XML**: `outputs/batch/Power/Power/Power_305/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 610: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [17-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-288] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-183] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-210] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-272] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-256] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-273] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-288] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-266] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [141-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-164] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-183] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-218] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-299] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-174] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-226] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-170] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-299] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-268] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-282] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [141-200] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [141-151] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-279] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-250] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-257] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-261] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [141-193] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-299] for track '24' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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