# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_77`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_77/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 32 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-80] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-119] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [95-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [102-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [95-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [95-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-46] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '23' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.