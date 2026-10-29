# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_28`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_28/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 328 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
> - Action 'Action_PreSnap' range [0-221] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-305] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-321] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-177] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-191] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-208] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-290] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-297] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-281] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-328] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [185-188] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [168-196] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [199-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-240] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-245] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-219] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-167] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [168-169] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [173-197] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [202-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 225, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [225-230] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [168-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [179-181] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [184-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [168-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [179-188] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [201-205] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [208-214] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-234] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-247] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-253] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-10] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-33] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-232] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-228] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-225] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-311] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-242] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-254] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-276] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-281] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-273] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-272] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.