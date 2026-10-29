# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_195`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_195/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-122] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-113] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-123] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-141] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-216] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-225] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-137] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-225] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-184] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-225] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-84] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [96-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [138-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-225] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-163] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-225] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-167] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-225] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-225] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-82] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [104-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [107-122] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [135-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-225] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' for track '18' starts at frame 94, but the player has no visible bounding box on this frame.
> - Action 'Action_ComboBlock' range [94-94] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [102-106] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-225] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-79] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-47] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-206] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-65] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-90] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-96] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-178] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-211] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-225] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-192] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-223] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-148] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-157] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-225] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-197] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-225] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-225] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-225] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-225] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-217] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-225] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-225] for track '33' has 3 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.