# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_227`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_227/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 208 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '0' (TE2) duration 115 frames exceeds threshold 90 frames [start=63, end=177].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (LG) duration 135 frames exceeds threshold 90 frames [start=43, end=177].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 135 frames exceeds threshold 90 frames [start=43, end=177].
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [42–72], lower_priority='Action_ZoneBlock' annotated_start=43, effective_Action_ZoneBlock_start=73.
> - Action 'Action_LeadBlock' range [63-88] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [91-162] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [168-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '0' starts at frame 178, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [178-178] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-192] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-198] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-423] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-226] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [234-235] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [245-250] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [256-258] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [260-261] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [263-267] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [275-291] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [299-300] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [308-414] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-275] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-302] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-230] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-268] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-449] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-186] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-255] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [258-268] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-449] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [43-80] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-86] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-239] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [42-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-226] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-261] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [263-268] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-277] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-305] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-405] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-449] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-85] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-198] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-230] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-236] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-258] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-199] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-449] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [42-302] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-197] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-247] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [43-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-236] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-277] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-284] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-298] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-192] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-267] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-278] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-301] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-309] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-327] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-330] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-186] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-231] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-245] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-268] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-411] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [419-439] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-280] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-301] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-331] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-410] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-230] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-373] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [376-378] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-449] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [43-85] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-108] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [43-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [42-72] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-74] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-230] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-236] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-248] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-291] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-302] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-315] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [96-230] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-104] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-287] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-314] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-124] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-258] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-285] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-322] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-338] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-259] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-273] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-259] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-302] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-312] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-366] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-297] for track '31' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-308] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-327] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-368] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [371-374] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-266] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-275] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-293] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-320] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [322-327] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-334] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-363] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [382-384] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-416] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-430] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-437] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-314] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-376] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-326] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-349] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-365] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-437] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-366] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-369] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-378] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-392] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [364-365] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-374] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-393] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-399] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-398] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-412] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-414] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-420] for track '41' has 2 frames without a visible bounding box.
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
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.