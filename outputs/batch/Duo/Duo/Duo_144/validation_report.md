# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_144`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_144/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 290: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-171] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-175] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-206] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [80-104] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-170] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-185] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-194] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-157] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-194] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [101-123] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-189] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-201] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-206] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' for track '9' starts at frame 80, but the player has no visible bounding box on this frame.
> - Action 'Action_ComboBlock' range [80-80] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-146] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-209] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-163] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-209] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [80-82] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [88-105] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [107-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [111-124] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-209] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-205] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-208] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-209] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-209] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-200] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-188] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-185] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-208] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '25' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.