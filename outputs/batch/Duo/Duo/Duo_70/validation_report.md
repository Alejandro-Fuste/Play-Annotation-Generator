# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_70`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_70/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 36 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-191] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-209] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-176] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-209] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-209] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [144-146] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [155-173] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [160-185] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-192] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-209] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-173] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-209] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '21' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.