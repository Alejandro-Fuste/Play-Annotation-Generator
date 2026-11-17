# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_124`
- **Input XML**: `outputs/batch/Power/Power/Power_124/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 250: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-193] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [81-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [92-102] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [108-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [137-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-126] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-115] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-130] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-172] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-98] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-165] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-197] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-200] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-205] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '22' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.