# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_57`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_57/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 125 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LG', 'LT', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 104: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-283] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-319] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-146] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-157] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-89] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-282] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-294] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-301] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-148] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-110] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-159] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-234] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-250] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-297] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-306] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-316] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-321] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-111] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-146] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-159] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-245] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-111] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-147] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-159] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-96] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-92] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-111] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-111] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-141] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-246] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-111] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-329] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-147] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-329] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-157] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-244] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-157] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-201] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-214] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-222] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-157] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-183] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-257] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-245] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-250] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-245] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-316] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-276] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-282] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-329] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-329] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-295] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-299] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-298] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-320] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-329] for track '40' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
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
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.