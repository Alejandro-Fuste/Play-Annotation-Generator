# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_146`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_146/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-76] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-209] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [94-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [113-117] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [82-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [90-91] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-138] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-132] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-81] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-134] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [82-87] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [102-103] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-138] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-209] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-209] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-113] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-8] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-13] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [83-103] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [107-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-109] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-209] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-168] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-209] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-208] for track '24' has 1 frames without a visible bounding box.
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
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.