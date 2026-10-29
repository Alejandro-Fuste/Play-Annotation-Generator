# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_71`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_71/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-185] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-209] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-209] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [120-132] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [137-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [144-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-195] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-209] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [120-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [125-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [132-135] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-209] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-190] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-197] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-203] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [120-163] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-197] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-172] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-185] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-171] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-181] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-209] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-184] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.