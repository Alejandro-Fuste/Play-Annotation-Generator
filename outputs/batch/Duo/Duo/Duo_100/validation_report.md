# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_100`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_100/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Action 'Action_PreSnap' range [0-240] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-247] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-261] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-241] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-262] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-224] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-236] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-252] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-220] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-261] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-184] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-201] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-212] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-226] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [160-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-242] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-221] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-54] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-240] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-238] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-240] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-247] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-254] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-266] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-236] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-251] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-224] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-242] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-266] for track '23' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.