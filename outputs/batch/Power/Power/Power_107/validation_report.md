# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_107`
- **Input XML**: `outputs/batch/Power/Power/Power_107/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 215: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - Row 216: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [15-196] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-164] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-285] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-291] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-259] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-171] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-297] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-189] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-223] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-230] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-299] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-218] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-264] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-271] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-274] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-294] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-281] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-169] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-231] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-242] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-247] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [97-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-231] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-241] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-105] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-112] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-117] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-233] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-299] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-201] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-201] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-226] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-215] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-274] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-225] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-286] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-295] for track '29' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.