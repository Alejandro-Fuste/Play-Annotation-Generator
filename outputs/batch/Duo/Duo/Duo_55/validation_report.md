# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_55`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_55/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 111: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - Row 112: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-106] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [70-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-147] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-179] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-146] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-69] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [76-79] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [84-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [88-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-147] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-156] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-179] for track '16' has 6 frames without a visible bounding box.
> - Action 'Action_ComboBlock' for track '17' starts at frame 70, but the player has no visible bounding box on this frame.
> - Action 'Action_ComboBlock' range [70-70] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [72-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [102-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [106-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [117-130] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-179] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-148] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [70-97] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-37] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-141] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-91] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-84] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-179] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-131] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-135] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-128] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-130] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-179] for track '31' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.