# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_19`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_19/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 34 |
| Ball Tracks | 7 |
| CSV events parsed | 22 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 40: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 40: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [244–258], lower_priority='Action_RunBlock' annotated_start=252, effective_Action_RunBlock_start=259.
> - Action 'Action_None' range [244-506] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [508-514] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-529] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-542] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [344-400] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-461] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [463-464] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-474] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [476-479] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-508] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [518-519] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-523] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [534-543] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-374] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-439] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [441-442] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-464] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-475] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [477-486] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-336] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-515] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-317] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-357] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [259-261] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [263-272] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-419] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-537] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [539-540] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-569] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [346-370] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-282] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-292] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [252-443] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [252-419] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-252] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-277] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-289] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-441] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-490] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-513] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [525-545] for track '18' has 5 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [252-331] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [333-381] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-522] for track '20' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [298-444] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-333] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-323] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [337-371] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-363] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-398] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [401-402] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-407] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-415] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-465] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [450-453] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-460] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-482] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-513] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-520] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-530] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [542-546] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-569] for track '38' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [557-569] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-569] for track '40' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.