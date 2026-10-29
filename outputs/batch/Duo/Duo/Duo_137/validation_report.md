# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_137`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_137/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 44 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 275: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-192] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-216] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-85] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-227] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-236] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [86-116] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-230] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-85] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [86-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-219] for track '25' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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