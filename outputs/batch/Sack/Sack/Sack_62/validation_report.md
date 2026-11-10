# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_62`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_62/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 47 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 126: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 126: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-150] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-174] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-161] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-171] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-202] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-68] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-110] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-124] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-210] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [133-159] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-163] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-160] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [183-208] for track '23' has 2 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.