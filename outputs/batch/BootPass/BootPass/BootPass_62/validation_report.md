# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_62`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_62/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_ThrowPass' for track '9' has invalid range: start=180, end=117. Clamping end to start.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [42–58], lower_priority='Action_RunBlock' annotated_start=50, effective_Action_RunBlock_start=59.
> - Segment 'Action_SecureCatch' for track '14' has invalid range: start=203, end=149. Clamping end to start.
> - Action 'Action_RunBlock' range [50-83] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [85-88] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [93-99] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-77] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-111] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-315] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-194] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-134] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [50-82] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [86-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [100-108] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [50-125] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-84] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-105] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-63] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-93] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-115] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-70] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [42-55] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [57-58] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [65-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [81-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [59-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-48] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [51-54] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [56-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-44] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-69] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-149] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-101] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-329] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-189] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-170] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-212] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-259] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-282] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-294] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-329] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-296] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-329] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-302] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-268] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-242] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-243] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-252] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-263] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-241] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-309] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-247] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-251] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-247] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-329] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-268] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-329] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-321] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-305] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-309] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-320] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-329] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-329] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-321] for track '41' has 2 frames without a visible bounding box.
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
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.