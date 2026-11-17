# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_295`
- **Input XML**: `outputs/batch/Power/Power/Power_295/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 590: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-146] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-212] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-254] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [85-106] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-194] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-213] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-160] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-265] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-201] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-136] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-269] for track '26' has 1 frames without a visible bounding box.
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