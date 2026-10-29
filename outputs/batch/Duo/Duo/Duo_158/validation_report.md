# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_158`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_158/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 47 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 298 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
> - Segment 'Action_ComboBlock' for track '18' has invalid range: start=178, end=20. Clamping end to start.
> - Action 'Action_PreSnap' range [0-59] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-298] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-237] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-251] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-290] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-251] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-254] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-258] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-251] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-235] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-204] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-228] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-237] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-261] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-206] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-213] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-233] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-285] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-276] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [178-219] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-286] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-294] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-219] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-254] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-297] for track '24' has 3 frames without a visible bounding box.
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