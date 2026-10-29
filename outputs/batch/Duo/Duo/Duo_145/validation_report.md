# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_145`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_145/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-109] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-138] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [100-110] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [115-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-117] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-143] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-137] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-165] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 134, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [134-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [100-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [111-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [116-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-146] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-173] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [100-105] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-147] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-31] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-39] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-161] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-159] for track '25' has 1 frames without a visible bounding box.
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