# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_175`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_175/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 352: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-185] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [112-139] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [145-165] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-176] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-182] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-164] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-209] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-205] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [112-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [140-141] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-185] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-193] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-111] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [112-117] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [120-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [135-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [153-154] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-209] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-163] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-209] for track '16' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-209] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-194] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [112-153] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-185] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-191] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-183] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-209] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-209] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-209] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-209] for track '28' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.